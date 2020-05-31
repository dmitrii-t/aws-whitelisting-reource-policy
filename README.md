## Synopsis
Pulumi AWS program to showcase whitelisting resource policy to allow specified IAM roles access secured secret. 
 
## Prerequisites
The project configures Pulumi as Docker image so the onlyy requirement is to have Docker installed.

## Getting started 
1. Create an `.env` at the root of the project specifying following environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_DEFAULT_REGION` 
    ```sh
    AWS_ACCESS_KEY_ID=<your access key id>
    AWS_SECRET_ACCESS_KEY=<your access key secret>
    AWS_DEFAULT_REGION=<aws reqin to deploy to>
    
    ```
1. Run Pulumi image with the following command to deploy the stack
    ```sh
    make pulumi up
    ```
    Deployed stack will have two IAM roles `TrustedRole`, `NoAccessRole`, a secret and a resource policy attached to the secret. 
    The resource policy will restrict access to `GetSecretValue` action to current user, root user and whoever assumes `TrusteedRole` only.
    Thus user assumed `NoAccessRole` wouldn't have accees to the secret value. 
    
    Feel free to assume roles `TrustedRole`, `NoAccessRole` and try to get secret value.
    
1. To cleanup deployed resources run
    ```sh
    make pulumi destroy
    ```