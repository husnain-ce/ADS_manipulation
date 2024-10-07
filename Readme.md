# Alternatve Data Streams Manipulation 

This script, from a cybersecurity perspective, is designed to manipulate and secure files through techniques such as copying files, adding hidden metadata using Alternate Data Streams (ADS) in the NTFS file system, and removing files in a controlled manner. Here’s a breakdown of its functionality and cybersecurity implications:

### Class: AdsSecurity

The class AdsSecurity encapsulates the security operations performed on files and directories, such as obfuscating or securing sensitive data, copying, and hiding data in files using NTFS-specific features like ADS.

### 1. __init__(self):

The constructor initializes the following components:

- File Path Management: It gathers a list of file paths (self.file_path_li) and extended file paths (self.ext_file_path) to operate on.
- Logical Drives Detection: The use of win32api.GetLogicalDriveStrings() is meant to fetch all logical drives, indicating that the class is designed to work across multiple storage devices and partitions in a Windows environment. This allows the tool to potentially scan and secure files across all available drives.


### 2. providing_security(self):

This method plays a critical role in scanning the file system for files that might need to be secured or processed. By walking through all files in the current working directory, it aims to:

- Gather File Information: The list self.file_path_li stores file paths for further operations. This could be viewed as an attempt to create a comprehensive inventory of all available files that may need security measures applied.
- Extend File Naming: It appends suffixes (0 and 1) to file paths, potentially to obfuscate the original files or create multiple versions of sensitive data. This could serve as a technique for data redundancy or backup in a secure manner.

Cybersecurity Implication: A file inventory is an important step for any security tool that deals with managing, securing, or monitoring files. Knowing what files exist and ensuring they are properly protected is crucial for defending against unauthorized access or tampering.

### 3. check_caller(self, callfrom):

This method performs the bulk of the security-related operations:

- File Duplication and Security: If callfrom is set to "create_secure", the script duplicates files to their extended versions (<file_path>0, <file_path>1). This could serve as a method to preserve sensitive data by creating backup versions, although without encryption or additional protection, it could pose risks.
- Alternate Data Streams (ADS): If callfrom is "add_more_secure", it uses ADS to store hidden metadata or content within the original file. ADS allows NTFS files to have hidden streams of data that are not visible in typical file explorers or by standard inspection tools.

### Cybersecurity Consideration:

- Hidden Data Streams: ADS is a powerful technique often used to hide data from the standard view. From a security perspective, this can be both a defensive and offensive tool:
- Defensive Use: Store critical security metadata or sensitive information in hidden streams, making it less accessible to attackers.
- Offensive Use: Malware often leverages ADS to hide malicious code or data, making detection harder for antivirus and forensic tools. This script, depending on its use, could be exploited for similar purposes, raising ethical concerns if misused.

### 4. create_secure_file(self):

This method acts as a file duplication and backup mechanism by calling check_caller() with "create_secure". The goal appears to be ensuring that secure copies of files are created, possibly to prevent data loss or tampering.

Cybersecurity Implication: Having redundant copies of sensitive files is a good security practice, but these copies must be properly secured (e.g., encrypted) to prevent unauthorized access. This script does not seem to implement encryption, which could lead to potential risks if the copies are not protected.

### 5. add_more_security(self):

This method appends data to the alternate data streams of files. As previously noted, the ADS mechanism allows files to hold hidden data streams in NTFS systems, a feature often used in cybersecurity to store hidden data for various purposes (such as metadata storage or to conceal critical information from attackers).

Cybersecurity Implication: While ADS can be a defensive technique, it also represents a risk, as attackers or malicious actors can use it to hide malware or unauthorized information. Thus, this functionality needs to be used with caution.

### 6. remove_file(self):

This method removes files that match the patterns *.*0 and *.*1. It walks through the current working directory and deletes extended files. This step likely serves as a cleanup mechanism, ensuring that extended or temporary files created during the security operations are removed after the task is done.

Cybersecurity Implication: File removal and cleanup are critical to preventing attackers from recovering sensitive information. However, this process needs to ensure that files are permanently removed, possibly using secure deletion methods to prevent recovery through forensic techniques.

### Potential Use Cases in Cybersecurity:

1.	File Integrity Protection: The duplication of files and the use of alternate data streams could be part of a strategy to protect file integrity. By hiding information in alternate streams, organizations can track modifications or store verification data securely.
2.	Malware Obfuscation: The method of hiding data in alternate data streams is commonly used by attackers to embed malicious payloads within legitimate-looking files. Security professionals need to be aware of such techniques to detect and mitigate these threats.
3.	Backup and Redundancy: Creating copies of sensitive files could be useful for creating secure backups, but the script should include encryption or other protective measures to ensure that sensitive data is not easily accessible in these copies.

### Conclusion:

This script showcases how Alternate Data Streams (ADS) in NTFS can be leveraged for file security, either by storing hidden data within a file or by creating redundant copies of sensitive files. However, from a cybersecurity perspective, it raises both defensive and offensive concerns:

- Defensive Use: Security professionals can use such techniques to protect sensitive metadata or create backups.
- Offensive Use: ADS can be misused by malicious actors to hide malware or unauthorized content, making it difficult for typical detection tools to uncover.



## Lib

- [win32api] - For Getting Drives
- [subprocess] - For manipulating Files

## Installation

```sh
git clone https://github.com/cyberdevo/Ads_Management.git

Either you can use built in exe file
```
### Task ToDo

- [x] Ads Manipulation
- [x] Make Anti Ads Boom
- [ ] Hide From Task Manager
- [ ] Bind With file and send it using email
- [ ] Add Custom Payload

## License

