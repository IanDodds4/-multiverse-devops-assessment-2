resource "aws_lb" "this" {
    name_prefix = "mvws9"
    internal = false
    load_balancer_type = "application"
    security_groups = [aws_security_group.alb.id]
    subnets = [for subnet in aws_subnet.public : subnet.id]
    tags = {
        Name = "multiverse"
    }
}

resource "aws_lb_listener" "http" {
    load_balancer_arn = aws_lb.this.arn
    port = "80"
    protocol = "HTTP"
    default_action {
        type = "forward"
        target_group_arn = aws_lb_target_group.http.arn
    }
}

resource "aws_lb_target_group" "http" {
    name_prefix = "mvws9"
    port = 80
    protocol = "HTTP"
    vpc_id = aws_vpc.this.id
    deregistration_delay = 0
}

resource "aws_launch_template" "this" {
    name_prefix = "mvws9"
    image_id = data.aws_ami.amazon_linux.id
    instance_type = "t3.micro"
    update_default_version = true
    user_data = base64encode(
        templatefile(
            "${path.module}/ec2-userdata.tftpl",
            { s3_bucket = aws_s3_bucket.this.id }
        )
    )

    iam_instance_profile {
        arn = aws_iam_instance_profile.this.arn
    }

    network_interfaces {
        associate_public_ip_address = true
        security_groups = [aws_security_group.ec2.id]
    }
}

resource "aws_autoscaling_group" "this" {
    name_prefix = "mvws9"
    max_size = 1
    min_size = 1
    health_check_grace_period = 30
    health_check_type = "ELB"
    desired_capacity = 1
    vpc_zone_identifier = [for subnet in aws_subnet.public : subnet.id]
    
    launch_template {
        id = aws_launch_template.this.id
        version = "$Latest"
    }

    tag {
        key = "Name"
        value = "multiverse"
        propagate_at_launch = true
    }

    instance_refresh {
        strategy = "Rolling"
        preferences {
            min_healthy_percentage = 50
        }
        triggers = ["tag"]
    }

    lifecycle {
        ignore_changes = [load_balancers, target_group_arns]
    }
}

resource "aws_autoscaling_attachment" "this" {
    autoscaling_group_name = aws_autoscaling_group.this.id
    lb_target_group_arn = aws_lb_target_group.http.arn
}
