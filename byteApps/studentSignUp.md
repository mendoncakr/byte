Application to increase workflow for prospective users interested in Byte Academy
======

Application needs to:

- Create Cohorts (Name, starting date, instructor)
- Add students (name, email, Github handle, passed challenge?, pre-work sent?, cohort) 
- if passed:
	- add to github team
	- send slack invite
	- send email with:
		Hey {{STUDENT_NAME}}, 

		Was great to meet you yesterday as well! First off, welcome to Byte Academy! We have some work and resources compiled for you on Github to get you prepared to hit the ground running when we start on {{COHORT_START_DATE}}.
		 
		If you don’t have a GitHub account already, please make an account and send me your username. Do this as soon as possible - all of our work is hosted on Github. You'll love it by the time we're through.

		If you haven't already, you will be shortly be receiving an invitation to our Slack channel. Any of the instructors (Ken, Greg, Billy) can answer any questions you have there.
		
		Looking forward to working with you!

		Best, 

		{{ COHORT_INSTRUCTOR }}
		
- if failed:
	- send email with with SO post asking to try again.
- List all cohorts
- List all students


##ICEBOX:

- Create cohort on Github through our app
- Edit email message