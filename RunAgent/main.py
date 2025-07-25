from uipath import UiPath

def main():
    sdk = UiPath()
    sdk.processes.invoke(
        "profservtenet",
        input_arguments={
            "message": "Hello, World!",
            "repeat": 3,
            "prefix": "[Echo]"
        },
        folder_path="sindhuja.m@uipath.com's workspace"
    )