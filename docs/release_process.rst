==========================
Production Release Process
==========================

The workflow below is targeted at creating a `GitHub release`_ using tags.

1. You will need to make sure that you are on the master branch, your working directory is clean and up to date.

2. Decide if you are going to increment the major, minor, or patch version. You can refer to semver_ to help you make
   that decision.

3. Use the `bump-major`, `bump-minor`, or `bump-patch`::

    $ make bump-minor

4. Once the task has successfully completed you need to push the tag and commit::

    $ git push origin && git push origin refs/tags/<tagname>

5. Create a release on GitHub. (`GitHub release`_)

.. _semver: https://semver.org
.. _GitHub release: https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release
