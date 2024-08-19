Incident Report: Web Stack Outage
Issue Summary:

On August 15, 2024 our e-commerce platform was down from 14:00 to 14:45 UTC. At this time, users are locked out and transactions were not going through. About 60% of users of the website were affected by this problem. They resulted from a misconfiguration of our load balancer in our server.

Timeline:

14:00 UTC – In monitoring system software, error rates were increased as well as servers had become unresponsive.
14:02 UTC – Multiple alert 500 Internal Server Errors.
14:05 UTC – Staking asset engineering team started working to find out what happened. The first manifestation was reported to be congestion in server systems.
14:14 UTC – Found that servers were working fine, had to search other components of applications.
14:20 UTC – attention was paid to the load balancer and it was identified that there were configuration issues.
14:30 UTC – Incident became somewhat more ‘serious’ for the DevOps team.
14:35 UTC – Wrong setting at the load balancer was also fixed.
14:45 UTC - Restoration of the service and elimination of the problem.
Root Cause and Resolution:

The outage was caused from a path issue in the load balancer, where the traffic distribution was wrong and many packages resulted in high errors rates as well as service unavailability. This problem was solved by going back to the previous load balancer setup and setting and using proper setting for correct handling of the flow of traffic.

Corrective and Preventative Measures:

Improvements:

Suggested improved mechanization of the configuration update process includes expansion of the testing process.
Enhance the level of monitoring so as to be able to identify configuration problems on real time.
Tasks:

Add the detailed scenarios as the part of the load balancer configuration document.
Perform other staging environment tests.
Include tests that check load balancer configuration settings as part of the loads for the CI/CD process.
It is recommended to configure precise regular reporting for load balancer parameters.
URL for Postmortem Report:

GitHub Repository Cloudezez/0x19-postmortem
Directory: 0x19-postmortem
File: README. md






