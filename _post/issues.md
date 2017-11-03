# Issues

1. Since the task name has to be unique, can you show how to raise an exception if the user enters a duplicate name?
1. Talk more about the native exception handling in Flask. Why did you decide to use Flask API since it simply is a wrapper on top of Flask - and, more specifically, Flask API exceptions are simply wrappers on top of the Flask exceptions. As a reader, I would like to know how applicable this tutorial is if I rip out Flask API and just use vanilla Flask, in other words.  
1. It's probably worth showing how to interact with the API using cURL.
1. What if I enter a string for the task id - http://localhost:5000/tasks/doesnotexist? Can you show how to handle this with a custom 404 page.
1. No try/except? I think we should show some sort of example that uses this since the pattern is commonly used. You could also dive into blanket catching exceptions (bare try/except). It saves time, but it can make your life harder as your app scales.
1. Thus far, we've just been in dev mode, with debug mode turned on. What about production? Are we handling errors correctly for a production environment? Maybe add a note to think about your audience - in dev mode you want to show more so that a developer can get the information needed to fix the issue but in production you just want to expose enough so that the end user doesn't exit the site.
1. Talk about logging. In prod, we need to get the full errors so that we can fix them.
1. What about `abort`? Is that ok to use?
1. Are we covering this objective - `Use Python exceptions in Flask`? Do we use the native Python exceptions?
1. Can you add a conclusion.
