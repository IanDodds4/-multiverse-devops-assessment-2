resource "aws_security_group" "alb" {
    name_prefix = "mvws9-alb"
    revoke_rules_on_delete = true
    vpc_id = aws_vpc.this.id
    tags = {
        Name = "multiverse-alb"
    }
}

resource "aws_security_group" "ec2" {
    name_prefix = "mvws9-ec2"
    revoke_rules_on_delete = true
    vpc_id = aws_vpc.this.id
    tags = {
        Name = "multiverse-ec2"
    }
}

resource "aws_security_group_rule" "alb_from_web_ingress" {
    type = "ingress"
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    security_group_id = aws_security_group.alb.id
}

resource "aws_security_group_rule" "alb_to_ec2_egress" {
    type = "egress"
    from_port = 80
    to_port = 80
    protocol = "tcp"
    source_security_group_id = aws_security_group.ec2.id
    security_group_id = aws_security_group.alb.id
}

resource "aws_security_group_rule" "ec2_from_alb_ingress" {
    type = "ingress"
    from_port = 80
    to_port = 80
    protocol = "tcp"
    source_security_group_id = aws_security_group.alb.id
    security_group_id = aws_security_group.ec2.id
}

resource "aws_security_group_rule" "ec2_to_web_egress" {
    type = "egress"
    from_port = 0
    to_port = 65535
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    security_group_id = aws_security_group.ec2.id
}
