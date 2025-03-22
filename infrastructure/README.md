

https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli
```
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
brew update
brew upgrade hashicorp/tap/terraform
```

https://cloud.google.com/sdk/docs/install


```
gcloud auth application-default login
```


```
terraform fmt -recursive
```

```
cd infrastructure/dev
terraform init
terraform plan
terraform apply
```