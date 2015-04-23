# Unmute

*This project is under construction.*

This project is dedicated to providing University of Michigan students a safe
space to voice their concerns about campus, local, or global affairs
anonymously. Our network has a more serious tone than other similar anonymous
sharing networks and is available to everyone on campus. 

We will implement:
- A responsive web application that can be used on both desktop and mobile
  browsers.
- An elegant user interface that connects stories with similar tag and color.
- An API that will allow us to implement native clients should the interest
  arise.

A Docker image is provided for quickly bootstrapping a working instance. It
can be used as follows:

    docker build -t *name* .
    docker run *name*

## Current Progress

Our backend is completely implemented, however, our frontend will require a
lot of additional steps. We will need to implement a UI for posting and
user accounts.
