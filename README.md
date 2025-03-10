# SMS Spam Dectector Project
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Made-with-Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
[![made-with-VS-Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?logo=visualstudiocode&logoColor=fff&style=plastic)](https://code.visualstudio.com/)

## Summary

This project aims to build a machine learning model to classify SMS messages as "spam" or "ham" (not spam) using TF-IDF vectorization and LinearSVC. It involves reading the "SMSSpamCollection" dataset, transforming text data into numerical features, and training a model to distinguish between spam and ham messages.

The process starts with data preprocessing, including cleaning, normalizing text, and splitting data into training and testing sets. TF-IDF vectorization converts text messages into numerical features, quantifying word importance.

A machine learning pipeline integrates TF-IDF vectorization and LinearSVC for streamlined text transformation and model training. The model is trained on the training set and evaluated on the testing set.

Finally, a user-friendly interface using Gradio allows users to input new SMS messages and receive real-time spam or ham predictions, making the model accessible for practical use.

## Files

| File | Function |                        
| ---- | ------------- |
| README.md | Project info |
| gradio_sms_text_classification.ipynb | Main project markup |
| sms_text_classification_solution.ipynb | Main project markup |
| Resources/SMSSpamCollection.csv| Data source |

## Documentation
https://pandas.pydata.org/docs/reference/frame.html

## Code of Conduct

This project has adopted the code of conduct defined by the Contributor Covenant to clarify expected behavior in our community.
For more information see the [Python Software Foundation Code of Conduct](https://policies.python.org/python.org/code-of-conduct/).


## Support

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
data-sourcing-challenge is an open-source project with a single maintainer. The best way to resolve your issue is to fix it yourself. Fork the repository and submit a pull request. 

### Get help

Ask the maintainer: [Chris Gilbert][1]

[1]: https://github.com/xraySMULu