module "common" {
  source = "../common"

  env        = local.env
  owner      = local.owner
  region     = local.region
  zone       = local.zone
  project_id = local.project_id
}
