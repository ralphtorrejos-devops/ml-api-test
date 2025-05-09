# PowerShell script to initialize and connect to new Git repository

# Initialize Git repository
git init

# Add new remote
git remote add origin https://github.com/ralphtorrejos-devops/mlops-api-test.git

# Add all files
git add .

# Commit changes
git commit -m "Initial commit"

# Push to main branch
git push -u origin main

Write-Host "Successfully initialized and connected to new repository!" 

#comment
