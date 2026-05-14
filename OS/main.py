import argparse
import os
import sys
import json
import subprocess

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_or_create_settings():
    root = get_project_root()
    settings_path = os.path.join(root, 'setting_DNTS.json')
    default_settings = {
        "default_language": "cpp",
        "openai_api_key": "",
        "openai_model": "gpt-4o",
        "ai_prompt": "You are an AI debugging assistant. The user's code encountered an issue.\n\nCode:\n{code}\n\nIssue Details:\n{error}\n\nPlease explain the cause of the issue and provide a corrected version of the code.",
        "quick_pack_filter": [".exe", ".o", ".out", ".class", "__pycache__"]
    }
    
    if not os.path.exists(settings_path):
        with open(settings_path, 'w', encoding='utf-8') as f:
            json.dump(default_settings, f, indent=4)
        return default_settings
    
    with open(settings_path, 'r', encoding='utf-8') as f:
        try:
            settings = json.load(f)
            # Merge missing keys
            updated = False
            for k, v in default_settings.items():
                if k not in settings:
                    settings[k] = v
                    updated = True
            if updated:
                with open(settings_path, 'w', encoding='utf-8') as fw:
                    json.dump(settings, fw, indent=4)
            return settings
        except json.JSONDecodeError:
            return default_settings

def run_test(instance_path, data_paths, settings):
    root = get_project_root()
    
    # Check if data_paths are directories or files
    test_batch_script = os.path.join(root, 'Test', 'test_batch.py')
    test_single_script = os.path.join(root, 'Test', 'test_single.py')
    
    for data_path in data_paths:
        abs_data_path = os.path.abspath(data_path)
        if os.path.isdir(abs_data_path):
            print(f"[OS] Running batch test on directory: {abs_data_path}")
            subprocess.run([sys.executable, test_batch_script, '--instance', instance_path, '--data_dir', abs_data_path])
        else:
            print(f"[OS] Running single test on file: {abs_data_path}")
            subprocess.run([sys.executable, test_single_script, '--instance', instance_path, '--input', abs_data_path])

def run_debug(instance_path, data_path, settings):
    root = get_project_root()
    debug_script = os.path.join(root, 'Debug', 'main.py')
    print(f"[OS] Starting debug on {instance_path} with data {data_path}")
    subprocess.run([sys.executable, debug_script, '--instance', instance_path, '--input', data_path])

def main():
    parser = argparse.ArgumentParser(description="T&DS Command Line Interface")
    parser.add_argument('-t', '--test', metavar='INSTANCE_PATH', help='Test instance path')
    parser.add_argument('-d', '--debug', metavar='INSTANCE_PATH', help='Debug instance path')
    parser.add_argument('-s', '--source', nargs='+', required=True, help='Data input path(s) or directories')
    
    args = parser.parse_args()
    
    settings = load_or_create_settings()
    
    if args.test:
        run_test(args.test, args.source, settings)
    elif args.debug:
        if len(args.source) > 1:
            print("[Error] Debug mode only supports a single data input path.")
            sys.exit(1)
        run_debug(args.debug, args.source[0], settings)
    else:
        print("[Error] Please specify either -t (test) or -d (debug).")
        parser.print_help()

if __name__ == '__main__':
    main()
