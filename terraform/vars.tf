variable "region" {
  description = "The AWS region for this project"
  default     = "eu-central-1"
}
variable "project" {
  description = "The name of the project"
  default     = "epam graduation"
}

variable "s_project" {
  description = "The short name of the project"
  default     = "EPAMGP"
}

variable "application" {
  description = "The name of application in the project"
  default     = "WeatherCollector"
}

variable "owner" {
  description = "The name of owner of creating resources"
  default     = "Aleksandr_Petrovskii1"
}


variable "vpc_cidr" {
  description = "VPC cidr block"
  default     = "10.0.0.0/16"
}

variable "subnets" {
  description = "AZ letters and subnets blocks for subnets"
  type        = map(any)
  default = {
    a = "10.0.0.0/24"
    b = "10.0.1.0/24"
    c = "10.0.2.0/24"
  }
}


variable "global_tags" {
  description = "Global tags. Will be on the most of resources"
  type        = map(any)
  default = {
    Application = "WeatherCollector"
    Terraform   = "true"
    Project     = "epam graduation"
    owner       = "Aleksandr_Petrovskii1"
  }
}
