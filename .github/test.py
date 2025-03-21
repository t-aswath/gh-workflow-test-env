import json
import os
import requests


def read_json_results(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
        data = json.loads(file_content)

    num_inputs = file_content.count("input")

    inputs = f"{num_inputs}\n" + "\n".join(entry["input"] for entry in data)
    outputs = "\n".join(entry["output"] for entry in data)

    return num_inputs, inputs, outputs


def validate_inputs_outputs(num_inputs, outputs):
    output_lines = outputs.strip().split("\n")
    if num_inputs == len(output_lines):
        print("Validation successful: num_inputs matches number of lines in outputs.")
    else:
        print(
            f"Validation failed: num_inputs ({num_inputs}) does not match number of output lines ({len(output_lines)})."
        )


def opencode(file_path):
    try:
        with open(file_path, "r") as file:
            code = file.read()
        print("File read successfully.")
        return code
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def send_python_to_judge0(source_code, test_input, test_output):
    return send_to_judge0(source_code, test_input, test_output, 71)  # Python 3


def send_java_to_judge0(source_code, test_input, test_output):
    return send_to_judge0(source_code, test_input, test_output, 62)  # Java


def send_cpp_to_judge0(source_code, test_input, test_output):
    return send_to_judge0(source_code, test_input, test_output, 54)  # C++


def send_to_judge0(source_code, test_input, test_output, language_id):
    url = "http://3c517df12106.ngrok.app/submissions/?base64_encoded=false&wait=true"

    payload = {
        "source_code": source_code,
        "language_id": language_id,
        "stdin": test_input,
    }

    response = requests.post(url, json=payload)

    error_log = f"{language_id}.log"

    if response.status_code == 201:
        result = response.json()
        judge_output = result.get("stdout", "").strip()
        expected_output = test_output.strip()

        if judge_output == expected_output:
            print("✅ Test Passed: Judge0 output matches expected output.")
        else:
            print("❌ Test Failed: Output does not match.")
            with open(error_log, "w") as f:
                f.write("Differences:\n")
                judge_lines = judge_output.split("\n")
                expected_lines = expected_output.split("\n")

                for i, (j_line, e_line) in enumerate(
                    zip(judge_lines, expected_lines), start=1
                ):
                    if j_line != e_line:
                        f.write(f"Line {i}:\n")
                        f.write(f"  Expected: {e_line}\n")
                        f.write(f"  Got:      {j_line}\n")

                if len(judge_lines) > len(expected_lines):
                    f.write("\nExtra lines in output:\n")
                    for i in range(len(expected_lines), len(judge_lines)):
                        f.write(f"  Line {i+1}: {judge_lines[i]}\n")
                elif len(judge_lines) < len(expected_lines):
                    f.write("\nMissing lines in output:\n")
                    for i in range(len(judge_lines), len(expected_lines)):
                        f.write(f"  Line {i+1}: {expected_lines[i]}\n")
    else:
        with open(error_log, "w") as f:
            f.write(f"❌ Error sending request to Judge0: {response.text}\n")


def main():
    print(list(os.listdir()))
    num_inputs, inputs, outputs = read_json_results("results.json")
    validate_inputs_outputs(num_inputs, outputs)
    python_source_code = opencode("code.py")
    cpp_source_code = opencode("code.cpp")
    java_source_code = opencode("code.java")

    if python_source_code:
        send_python_to_judge0(python_source_code, inputs, outputs)
    if cpp_source_code:
        send_cpp_to_judge0(cpp_source_code, inputs, outputs)
    if python_source_code:
        send_java_to_judge0(java_source_code, inputs, outputs)


if __name__ == "__main__":
    main()
