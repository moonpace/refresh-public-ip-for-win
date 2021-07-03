call activate [PATH]
"C:\Users\moonpace\AppData\Local\Programs\Python\Python39\python.exe" "%~dp0/upip.py"
"c:\Program Files\Amazon\AWSCLIV2\aws.exe" s3 cp "%~dp0/public_ip.txt" "s3://theethru-ats/public_ip.txt"