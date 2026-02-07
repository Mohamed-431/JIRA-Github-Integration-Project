# JIRA-Github-Integration-Project

## Project Overview

This project provides a seamless integration between GitHub and JIRA, enabling teams to automate the creation of JIRA tickets by simply commenting "/jira" on any Github issue. Behind the scenes, a Flask webhook server detects the comment and creates a corresponding JIRA ticket with all the relevant information.

## Project Architecture

![App Screenshot](https://image2url.com/r2/default/images/1769606223863-ed2f2c68-5806-4430-9d2f-964c3c31bdf6.png) 

## Tools Used 

- AWS Cloud Infrastructure 
- Python 3 + Flask
- GitHub Webhooks
- JIRA REST API


## Functioning Project

### GitHub Issue

**Before:**
![](https://image2url.com/r2/default/images/1770495085408-2d850bbd-b5b2-4af4-b593-ab3b586f6981.png)

**After:**
![](https://image2url.com/r2/default/images/1770495155390-a61a2578-a284-45e0-a358-0817e379c947.png)

---

### JIRA

**Before:**
![](https://image2url.com/r2/default/images/1770495302750-5168f07a-9982-4c05-b8dd-9ce5cf418fd8.png)

**After:**
![](https://image2url.com/r2/default/images/1770495442568-615d34bc-a51d-42c9-87c1-d1989c0ef222.png)

---

### Flask Webhook Server

**Before:**
![](https://image2url.com/r2/default/images/1770495726530-f5d703a6-5ae4-4ead-9e74-acf43d4da0a3.png)

**After:**
![](https://image2url.com/r2/default/images/1770495996890-6ed86adf-c25d-4246-a4b3-b2c48e39e9fd.png)


## What is the need for this project?

Every day, developers can go through hundreds of GitHub issues to identify legitimate problems that need to be addressed. Once they find a valid issue, they would have to manually create a JIRA ticket for it, a process that can take up to 5 minutes per ticket and forces developers to constantly jump between GitHub and JIRA. This project fixes that problem. Instead of manually creating tickets, developers can simply comment "/jira" on a GitHub issue, and a JIRA ticket with all relevant information is created instantly. Therefore, developers no longer waste time on manual ticket creation and can instead dedicate more of their efforts to actual development work.

## Summary

In summary, this project successfully achieved its objective of automating the creation of JIRA tickets from GitHub issues in an event-driven manner. By utilising Flask to develop the webhook server and the requests library to communicate with JIRA's REST API, I have also been able to demonstrate my Python expertise. Finally, by bridging the gap between GitHub and JIRA with the implementation of webhooks and cloud infrastructure, this project has also enabled me to showcase my comprehensive understanding of DevOps automation principles.







