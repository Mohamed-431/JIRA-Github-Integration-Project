# JIRA-Github-Integration-Project

## Project Overview

This project provides a seamless integration between GitHub and JIRA, enabling teams to automate the creation of JIRA tickets by simply commenting "/jira" on any Github issue. Behind the scenes, a Flask webhook server detects the comment and creates a corresponding JIRA ticket with all the relevant information.

## Project Architecture

![](https://snipboard.io/ZKinuC.jpg) 

## Tools Used 

- AWS Cloud Infrastructure 
- Python 3 + Flask
- GitHub Webhooks
- JIRA REST API


## Functioning Project

### GitHub Issue

**Before:**
![](https://snipboard.io/8QfBLp.jpg)

**After:**
![](https://snipboard.io/3G5pv4.jpg)

---

### JIRA

**Before:**
![](https://snipboard.io/gvQdh6.jpg)

**After:**
![](https://snipboard.io/eGXH8P.jpg)

---

### Flask Webhook Server

**Before:**
![](https://snipboard.io/0c1VuU.jpg)

**After:**
![](https://snipboard.io/VX1pN7.jpg)


## What is the need for this project?

Every day, developers can go through hundreds of GitHub issues to identify legitimate problems that need to be addressed. Once they find a valid issue, they would have to manually create a JIRA ticket for it, a process that can take up to 5 minutes per ticket and forces developers to constantly jump between GitHub and JIRA. This project fixes that problem. Instead of manually creating tickets, developers can simply comment "/jira" on a GitHub issue, and a JIRA ticket with all relevant information is created instantly. Therefore, developers no longer waste time on manual ticket creation and can instead dedicate more of their efforts to actual development work.

## Summary

In summary, this project successfully achieved its objective of automating the creation of JIRA tickets from GitHub issues in an event-driven manner. By utilising Flask to develop the webhook server and the requests library to communicate with JIRA's REST API, I have also been able to demonstrate my Python expertise. Finally, by bridging the gap between GitHub and JIRA with the implementation of webhooks and cloud infrastructure, this project has also enabled me to showcase my comprehensive understanding of DevOps automation principles.







