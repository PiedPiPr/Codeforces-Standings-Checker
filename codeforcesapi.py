import requests
import json


#Inputs for ContestId and UserId
print("Please enter the Contest ID and press inter")
contest_in = int(input())

print("Enter the problem ID/Index - A B C D E F (enter space for multiple problems)")
problem_in = input()
problem_in = problem_in.upper()
problem_in = problem_in.split()

print("Now enter the user handles and press enter (enter space for multiple users)")
handles_in = input()
handles_in = handles_in.split()

#Main Logic For Finding Result
points = []
result_status = []
for i in handles_in:
	api = requests.get("https://codeforces.com/api/user.status?handle=%s&from=1"%(i))
	data = api.json()
	count = 0
	rslt_status = []
	for j in data['result']:
		cntst = j['problem']['contestId']
		if cntst == contest_in:
			for k in problem_in:
				if k == j['problem']['index']:
					rslt = j['verdict']
					if rslt == ("OK"):
						count +=1
						rslt_status.append("Correct")
					else:
						rslt_status.append("N/A")
	points.append(int(count))
	result_status.append(rslt_status)

print(handles_in)
print(points)
print(result_status)