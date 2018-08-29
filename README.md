# LevelUp-35 Git and Pivotal tracker Integration
This is intended to illustrate the integration of you git with pivotal Tracker
just so to help making the work easier and also easily reflect and track your progress
on both platforms (Git and Pivotal Tracker)

### Prerequisites
All that you need is an account on both platforms, that is to say

# 1. Pivotal Tracker
![alt text](https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_1489708427/pivotal-tracker.png)
### Procedures
1. Navigate to the user profile page
2. scroll and find the API Token section
  The API Token will look a lot like the sample below.
  ```
  **API TOKEN** 0f360a879fcf7425135f7ddef076e431
  ```
and then copy the api token to your clip board.
# 2. Github
![alt text](http://afrisoft.co.ke/wp-content/uploads/2017/11/github.png)
When you switch back to your git, navigate to the settings of the repository
you are working with,
On the left side of page, check the options listed as below
> Collaborators
> Branches
> Webhooks
> Integrations & services
> Debloy Keys

On the option above select
```
Integrations & services
```
1. locate the services section and select add service.
2. Search and locate pivotal Tracker in the dropdown
3. enter the API Token in the API field from the provided fields and save the changes.

### Finally.
The final step is all about the way you write your commit message.
the format of writing the commit message should be as follows.

```
git commit -m "Your commit message [Task ID]"
```
*Replace **Task ID** with the id of your task from pivotal Tracker*

And when you push your work to the web, the changes you have made will be reflectd in pivotal tracker
under the task who's ID you used in the commit message.

Thank your
* Edmond Sylar.
