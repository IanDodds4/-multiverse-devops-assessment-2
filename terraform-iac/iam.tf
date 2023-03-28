data "aws_iam_policy_document" "assume_role" {
    statement {
        actions = ["sts:AssumeRole"]
        effect = "Allow"
        principals {
            type = "Service"
            identifiers = ["ec2.amazonaws.com"]
        }
    }
}

data "aws_iam_policy_document" "ec2" {
    statement {
        effect = "Allow"
        actions = ["s3:*"]
        resources = ["arn:aws:s3:::*"]
    }
}

resource "aws_iam_role" "this" {
    name_prefix = "mvws9"
    assume_role_policy = data.aws_iam_policy_document.assume_role.json
    tags = {
        Name = "multiverse"
    }
}

resource "aws_iam_policy" "this" {
    name_prefix = "mvws9"
    path = "/"
    policy = data.aws_iam_policy_document.ec2.json
    tags = {
        Name = "multiverse"
    }
}

resource "aws_iam_policy_attachment" "this" {
    name = "mvws9"
    roles = [aws_iam_role.this.name]
    policy_arn = aws_iam_policy.this.arn
}

resource "aws_iam_instance_profile" "this" {
    name_prefix = "mvws9"
    role = aws_iam_role.this.name
}
