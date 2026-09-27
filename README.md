Navigate to the index.html page to find the codes for portfolio. 

***While I upload the updated Resume everytime, please find out that there may be a network isssue and the deployment might be late.***

Deployment: In GitHub Settings > Pages > Build and deployment, set Source to GitHub Actions. The deploy-pages workflow publishes pushes to main or master and stamps the footer with the deployment build date in India time (day, month, year). Commit index.html, scripts/build_site.py, .github/workflows/deploy-pages.yml, and .gitignore together. Local source displays Pending deployment; python scripts/build_site.py generates the dated preview in _site/index.html.

