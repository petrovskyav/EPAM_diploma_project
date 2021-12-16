resource "aws_eks_cluster" "example" {
  name     = "pa-test-eks-cluster"
  role_arn = "arn:aws:iam::156001095759:role/eks_role"

  vpc_config {
    subnet_ids = ["subnet-18068254", "subnet-dc4a30b6", "subnet-2965d455"]
  }
  tags = {
    owner = "Aleksandr_Petrovskii1@epam.com"
  }
}


resource "aws_eks_node_group" "example" {
  cluster_name    = aws_eks_cluster.example.name
  node_group_name = "pa-test-node-group"
  node_role_arn   = "arn:aws:iam::156001095759:role/EKS_nodegroup_role"
  subnet_ids      = ["subnet-18068254", "subnet-dc4a30b6", "subnet-2965d455"]
  instance_types = ["t3.small"]

  scaling_config {
    desired_size = 1
    max_size     = 1
    min_size     = 1
  }

  update_config {
    max_unavailable = 1
  }
  tags = {
    owner = "Aleksandr_Petrovskii1@epam.com"
  }
}
