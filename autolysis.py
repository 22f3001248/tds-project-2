#uv start
# /// script
# requires-python = ">=3.6"
# dependencies = [
#   "httpx",
#   "pandas",
#   "matplotlib",
#   "seaborn",
#   "Pillow",
# ]
# ///
import sys
import pandas as pd
import os
import httpx
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
matplotlib.use("Agg")

def create_output_structure(dataset_name):
    dataset_dir = os.path.join(os.getcwd(), dataset_name[:-4])
    os.makedirs(dataset_dir, exist_ok=True)
    readme_file = os.path.join(dataset_dir, "README.md")

    if not os.path.exists(readme_file):
        with open(readme_file, "w") as f:
            f.write(f"# {dataset_name} Dataset\n\nAnalysis for the {dataset_name} dataset.\n")

    return dataset_dir

def load_data(file_path):
    try:
        data = pd.read_csv(file_path, encoding='latin-1')
        print(f"Dataset loaded: {file_path}")
        print(data.info())
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

def generic_analysis(data):
    summary = {
        "columns": data.columns.tolist(),
        "data_types": data.dtypes.to_dict(),
        "missing_values": data.isnull().sum().to_dict(),
        "summary_statistics": data.describe(include='all').to_dict()
    }
    return summary

def ask_llm(prompt, functions=None, dry_run=False):
    if dry_run:
        print(f"Simulating API call with prompt: {prompt}")
        return {"choices": [{"message": {"content": "Test response this is the story"}}]}
    
    headers = {"Authorization": f"Bearer {os.environ['AIPROXY_TOKEN']}"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "functions": functions,
    }
    timeout = httpx.Timeout(10.0, read=None)
    
    try:
        response = httpx.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers, json=payload, timeout=timeout)
        response.raise_for_status()
        response_data = response.json()

        if "choices" in response_data:
            return response_data["choices"][0]["message"]["content"]
        else:
            print(f"Error: No 'choices' found in response: {response_data}")
            return None
    except httpx.RequestError as e:
        print(f"Request error: {e}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return None

def analyze_with_llm(data_summary):
    prompt = f"Here is a summary of a dataset:\n{data_summary}. Suggest insightful analysis and provide a narrative."
    response = ask_llm(prompt)
    return response

def visualize_data(data, file_name, dataset_dir):
    try:
        numeric_data = data.select_dtypes(include=['int64', 'float64'])
        correlation_matrix = numeric_data.corr()
        plt.figure(figsize=(5.12, 5.12))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
        
        # Better naming
        output_file = os.path.join(dataset_dir, f"{file_name[:-4]}_correlation_heatmap.png")
        
        plt.title("Correlation Heatmap")
        plt.savefig(output_file, dpi=100, bbox_inches='tight', pad_inches=0.1)
        plt.close()
        
        # Resizing images
        with Image.open(output_file) as img:
            width, height = img.size
            max_size = 512
            if width > height:
                new_width = max_size
                new_height = int((max_size / width) * height)
            else:
                new_height = max_size
                new_width = int((max_size / height) * width)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            img.save(output_file)
    except Exception as e:
        print(f"Error in visualization: {e}")
        sys.exit(1)
        
def create_story(data_summary, insights, images):
    prompt = f"""
    Write a report for the dataset based on the following analysis:
    Summary: {data_summary}
    Insights: {insights}
    Visualizations: {images}
    Format it as a markdown story.
    """
    response = ask_llm(prompt)
    print("response:",response)
    return response

def save_results(story,dataset_dir):
    with open(os.path.join(dataset_dir, "README.md"), "a") as file:
        file.write(story)
    print("Saved README.md with the analysis.")


if __name__ == "__main__":
    file_path = sys.argv[1]
    dataset_dir=create_output_structure(file_path)
    data = load_data(file_path)
    summary = generic_analysis(data)
    insights = analyze_with_llm(summary)
    visualize_data(data, file_path, dataset_dir)
    story = create_story(summary, insights, ["output.png"])
    save_results(story,dataset_dir)

#uv end