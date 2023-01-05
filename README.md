# privacy_intent_classifier
Privacy Policy Intent Classifier with Docker, FastAPI, uvicorn, and Huggingface Spaces

## Desciption

Designed to split privacy policies into individual sentences and classify their intent. The app allows users to input a privacy policy and receive a breakdown of the policy's content and its underlying intentions.It uses Docker containers and FastAPI to process and analyze the policies. Huggingface space hosts the app. 

**App link :** https://huggingface.co/spaces/remzicam/privacy_intent

**Model link:** https://huggingface.co/remzicam/privacy_intent

5 Intents:

*(1) Data Collection/Usage: What, why and how user information is collected;*

*(2) Data Sharing/Disclosure: What, why and how user information is shared with or collected by third parties;*

*(3) Data Storage/Retention: How long and where user information will be stored;*

*(4) Data Security/Protection: Protection measures for user information;*

*(5) Other: Other privacy practices that do not fall into the above four categories.*

For more info: https://aclanthology.org/2021.acl-long.340/

## Business Problem 

Privacy policies can be difficult for users to understand, leading to mistrust between companies and their customers. This app aims to address this problem by providing a simple and easy-to-use tool for breaking down privacy policies into individual sentences and classifying their intent.

## Dataset

[PolicyIE]([https://duckduckgo.com](https://aclanthology.org/2021.acl-long.340/)).

## Model
PrivBERT model is fine-tuned for this task.

F1 Score: 88 (%4 performance increase compared to original work)

## Tools used

• docker: to package the app and its dependencies into a container, allowing it to be easily deployed and run

• fastapi: building APIs with Python and interacting with it through simple HTTP requests.

• transformers: model finetuning

• datasets: to load and manipulate the data
