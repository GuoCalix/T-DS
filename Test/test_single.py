import argparse
import os
import subprocess
import tempfile
import sys
import shutil

def init_args():
    parser = argparse.ArgumentParser(description='Generic Judger for T&DS')
    parser.add_argument('--instance', required=True, help='Path to the source code (.cpp, .py, etc.)')
    parser.add_argument('--input', required=True, help='Path to the input data file (.in)')
    parser.add_argument('--standard', required=False, help='Path to the standard output file (.out)')
    parser.add_argument('--timeout', default=2.0, type=float, help='Timeout in seconds')
    return parser.parse_args()

def standard_judger(answer_file, std_file):
    with open(std_file, 'r', encoding='utf-8') as f:
        c_std = [line.rstrip() for line in f.read().splitlines()]
    with open(answer_file, 'r', encoding='utf-8') as f:
        c_answer = [line.rstrip() for line in f.read().splitlines()]
        
    if len(c_std) != len(c_answer):
        return False, f'File length differs: Expected {len(c_std)} lines, got {len(c_answer)} lines'
        
    for idx, (lin_std, lin_ans) in enumerate(zip(c_std, c_answer)):
        if lin_std != lin_ans:
            return False, f'Wrong answer found at Line {idx + 1}:\nExpected: {lin_std}\nGot     : {lin_ans}'
            
    return True, 'Correct'

def run_test(instance, input_file, standard_file, timeout):
    if not os.path.exists(instance):
        return {"status": "Error", "message": "Source code not found"}
    if not os.path.exists(input_file):
        return {"status": "Error", "message": "Input file not found"}
    if standard_file and not os.path.exists(standard_file):
        return {"status": "Error", "message": "Standard output file not found"}

    ext = os.path.splitext(instance)[1].lower()
    workdir = tempfile.mkdtemp()
    
    try:
        if ext == '.cpp' or ext == '.c++' or ext == '.cc':
            exec_file = os.path.join(workdir, 'program.exe' if os.name == 'nt' else 'program')
            compile_cmd = ['g++', instance, '-o', exec_file, '-O2', '-Wall', '-std=c++17']
            try:
                subprocess.run(compile_cmd, check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                return {"status": "CompileError", "message": e.stderr}
            run_cmd = [exec_file]
        elif ext == '.py':
            run_cmd = [sys.executable, instance]
        else:
            return {"status": "Error", "message": f"Unsupported language extension: {ext}"}

        output_file = os.path.join(workdir, 'output.out')
        
        with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
            try:
                subprocess.run(run_cmd, check=True, timeout=timeout, stdin=fin, stdout=fout, stderr=subprocess.PIPE, text=True)
            except subprocess.TimeoutExpired:
                return {"status": "TimeLimitExceeded", "message": "Out of Time Limit!"}
            except subprocess.CalledProcessError as e:
                return {"status": "RuntimeError", "message": f"Runtime Error with returncode {e.returncode}\n{e.stderr}"}

        if standard_file:
            passed, msg = standard_judger(output_file, standard_file)
            if passed:
                return {"status": "Accepted", "message": msg}
            else:
                return {"status": "WrongAnswer", "message": msg, "wrong_output_file": output_file}
        else:
            # If no standard file, we just test if it runs without errors
            return {"status": "Success", "message": "Execution finished successfully without validation against standard output."}
            
    finally:
        # Note: if we want to keep wrong output for OpenAI, we shouldn't delete the temp directory completely,
        # or we should copy the output file back. For now, we will read it and include in the message if needed.
        shutil.rmtree(workdir, ignore_errors=True)

if __name__ == '__main__':
    args = init_args()
    
    # Infer standard_file if not provided
    std_file = args.standard
    if not std_file:
        in_path, in_ext = os.path.splitext(args.input)
        if in_ext == '.in':
            inferred = in_path + '.out'
            if os.path.exists(inferred):
                std_file = inferred

    result = run_test(args.instance, args.input, std_file, args.timeout)
    print(f"[TEST_RESULT] {result['status']}: {result['message']}")
    if result['status'] != 'Accepted' and result['status'] != 'Success':
        sys.exit(1)