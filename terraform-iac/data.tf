data "aws_availability_zones" "eu_west_2" {
    state = "available"
    
    filter {
        name = "region-name"
        values = ["eu-west-2"]
    }

    filter {
        name = "opt-in-status"
        values = ["opt-in-not-required"]
    }
}

data "aws_ami" "amazon_linux" {
    most_recent = true
    owners = ["amazon"]
    filter {
        name = "name"
        values = ["amzn2-ami-hvm-*-gp2"]
    }

    filter {
        name = "root-device-type"
        values = ["ebs"]
    }

    filter {
        name = "virtualization-type"
        values = ["hvm"]
    }
    
    filter {
        name = "architecture"
        values = ["x86_64"]
    }
}