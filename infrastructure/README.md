```markdown
# Infrastructure Setup

This document provides instructions to set up the infrastructure using Terraform and Google Cloud SDK.

## Prerequisites

1. Install Terraform CLI:
   [Terraform Installation Guide](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli)

   ```sh
   brew tap hashicorp/tap
   brew install hashicorp/tap/terraform
   brew update
   brew upgrade hashicorp/tap/terraform
   ```

2. Setup Google Cloud SDK:
   [Google Cloud SDK Installation Guide](https://cloud.google.com/sdk/docs/install)

   Init to project:
 ```sh
    gcloud init  
   ```
   And authenticate:
   ```sh
   gcloud auth application-default login
   ```

## Formatting Terraform Code

To format the Terraform code recursively, run:

```sh
terraform fmt -recursive
```

## [LOCAL] Initialize and Apply Terraform Configuration 

Navigate to the `infrastructure/dev` directory and run the following commands:

```sh
cd infrastructure/dev
terraform init
terraform plan
terraform apply
```
