resource "aws_eks_cluster" "example" {
  name     = "example"
  role_arn = "arn:aws:iam::156001095759:role/eks_role"

#  vpc_id = "vpc-6c6dfe06"
  vpc_config {
    subnet_ids = ["subnet-18068254", "subnet-dc4a30b6", "subnet-2965d455"]
  }
}
