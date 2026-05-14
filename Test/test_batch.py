import argparse
import os
import sys

# Import the run_test logic from test_single
from test_single import run_test

def init_args():
    parser = argparse.ArgumentParser(description='Generic Batch Judger for T&DS')
    parser.add_argument('--instance', required=True, help='Path to the source code (.cpp, .py, etc.)')
    parser.add_argument('--data_dir', required=True, help='Directory containing the test data (.in and .out files)')
    parser.add_argument('--timeout', default=2.0, type=float, help='Timeout in seconds')
    return parser.parse_args()

def run_batch(instance, data_dir, timeout):
    if not os.path.isdir(data_dir):
        print(f"[Error] Data directory not found: {data_dir}")
        return False

    files = os.listdir(data_dir)
    in_files = set(f for f in files if f.endswith('.in'))
    out_files = set(f for f in files if f.endswith('.out'))

    # Check for NotFoundOut error
    for in_file in in_files:
        base_name = in_file[:-3]
        if f"{base_name}.out" not in out_files:
            print(f"[Warning] {in_file}: NotFoundOut error")

    # Check for NotFoundIn error
    for out_file in out_files:
        base_name = out_file[:-4]
        if f"{base_name}.in" not in in_files:
            print(f"[Warning] {out_file}: NotFoundIn error")

    # Only test pairs that have both
    valid_pairs = sorted([f[:-3] for f in in_files if f"{f[:-3]}.out" in out_files])
    
    if not valid_pairs:
        print("[Info] No valid test pairs (.in and .out) found to test.")
        return False

    all_passed = True
    for base in valid_pairs:
        input_file = os.path.join(data_dir, f"{base}.in")
        standard_file = os.path.join(data_dir, f"{base}.out")
        
        print(f"\n--- Testing {base} ---")
        result = run_test(instance, input_file, standard_file, timeout)
        print(f"Result: {result['status']}")
        if result['status'] != 'Accepted':
            all_passed = False
            print(f"Details: {result['message']}")
            
    if all_passed:
        print("\n[Summary] All test instances are working well.")
    else:
        print("\n[Summary] Some tests failed.")
        
    return all_passed

if __name__ == '__main__':
    args = init_args()
    success = run_batch(args.instance, args.data_dir, args.timeout)
    if not success:
        sys.exit(1)
