TEMPLATE = """
Please analyze the following CV text and extract the key information. Structure the output in the following format without any label or prefix:
{
    "Name": "Extract the full name from {file_path} and convert it to Vietnamese language.",
    "Birth_date": "Extract Birth date from CV following day/month/year.",
    "Address": "Extract the address from the CV text.",
    "Self_introduction": "Extract a brief self-introduction or career goals.",
    "Education": "Extract the education background from the CV text.",
    "Skills": "Extract the key skills mentioned in the CV.",
    "Project": [
        {
            "Name_project": "Extract the project name (if available).",
            "Tool_technology": "Extract the tools and technologies used in the project.",
            "Job_descriptions": "Summarize the responsibilities or job descriptions related to the project."
        },
        {
            "Name_project": "Extract another project name (if available).",
            "Tool_technology": "Extract the tools and technologies used in this project.",
            "Job_descriptions": "Summarize the responsibilities or job descriptions related to this project."
        }
    ],
    "Work_experience": [
        {
            "Name_company": "Extract the company name.",
            "Role": "Extract the role or job title held at the company.",
            "Working_period": "Extract the duration of employment (day/month/year)."
        },
        {
            "Name_company": "Extract another company name (if available).",
            "Role": "Extract another role or job title held at the company.",
            "Working_period": "Extract the duration of employment (day/month/year)."
        }
    ],
    "cv_path": "{full_file_path}",
}
Resume text: {cv_text}
Please return the extracted information in the specified format. Do not include any labels or prefixes in the output. If there are any unclear contents, please automatically correct them. The output should be in English. If there are formatting errors, correct them to ensure the output is valid JSON.
"""
