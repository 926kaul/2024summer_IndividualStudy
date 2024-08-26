# Vulnerability Search and Study with ChatGPT, GPT Plugins, and Custom GPTs

## 1st Week
- **Activities**:
  - Searched and studied known vulnerabilities.
  - Reproduced situations related to these vulnerabilities.
  - Tracked requests and responses to understand potential issues.

## 2nd Week
- **Activities**:
  - Studied the paper: Su, Dongxun, et al. "GPT Store Mining and Analysis" ([arXiv preprint arXiv:2405.10210](https://arxiv.org/abs/2405.10210)).
  - Conducted experiments to understand privacy issues.

## 3rd Week
- **Activities**:
  - Categorized potential security threats in Custom GPTs, referencing the paper by Guanhong Tao et al. "Opening A Pandora’s Box: Things You Should Know in the Era of Custom GPTs" ([arXiv preprint arXiv:2401.00905](https://arxiv.org/abs/2401.00905)).
  - Created a Phishing GPT and a Phishing website to test security vulnerabilities.
  - Mimicked the "AI Humanizer" GPT from the GPT Store and tested its effectiveness in phishing.
  - Successfully captured victim's ID and password through the phishing website.

## 4th Week
- **Activities**:
  - Attempted to trigger XSS via HTML and JS execution but failed due to Custom GPTs only supporting Python interpreters.
  - Discovered through experiments that Custom GPTs need Python support to provide download links for knowledge files.
  - Explored methods to extract and investigate the instructions and knowledge files of GPTs in the GPT Store for malicious intent.
  - Considered approaches to distinguish and investigate similar GPTs in the Store.

## 5th Week
- **Activities**:
  - Conducted manual inspections of the top 10 ranked GPTs and similar GPTs.
  - Classified GPTs based on the inclusion of malicious keywords in their instructions.
  - Resolved issues with GPTs refusing to provide instructions by using Base64 encoded prompts (Jailbreaking).
  - Implemented crawling to automatically extract instructions from GPTs in the GPT Store.

## 6th Week
- **Activities**:
  - Collected data from the top 500 GPTs and up to 5 similar GPTs for each.
  - Extracted and classified URLs found in the instructions.
  - Investigated whether any GPTs were promoting external URLs.

## 7th Week
- **Activities**:
  - Monitored the URLs of the top 500 GPTs and related GPTs for changes, but found none.
  - Manually checked URLs for any malicious content, and categorized suspicious URLs or features.
  - Analyzed the similarity between instructions of 1159 GPTs using TF-IDF vector cosine similarity.
  - Identified and manually reviewed copycat GPTs with similarity scores above 0.6.

## 8th Week
- **Activities**:
  - Continued monitoring URLs in GPT instructions but observed no changes.
  - Investigated developers like PI DINGHAI, xxyyai.com, and Sora, suspected of creating copycat GPTs.
  - Hypothesized that these developers might aim to increase traffic, create pirated versions of other GPTs, or collect user conversations.
  - Attempted to leak access tokens by creating a GPT linked with Google Calendar but failed due to limitations in API and schema structures.

## 9th Week
- **Activities**:
  - Investigated copycat GPT developer Sora and associated GPTs connected to chat-prompt.com.
  - Analyzed the instructions of approximately six copycat GPTs and identified triggers leading to requests to chat-prompt.com.
  - Found that the API schema of these GPTs was likely designed to collect user conversations.
  - Additionally, identified that the responses from chat-prompt.com appeared to promote specific GPTs or websites.
  - Modified OAuth and API schema structures in GPTs linked to Google Calendar, but access token leakage remained unresolved.
