resource "aws_vpc" "this" {
    cidr_block = "10.0.0.0/16"
    enable_dns_support = true
    enable_dns_hostnames = true
    tags = {
        Name = "multiverse"
    }
}

resource "aws_subnet" "public" {
    for_each = toset(["1", "2"])
    vpc_id = aws_vpc.this.id
    cidr_block = "10.0.${each.key}.0/24"
    availability_zone = element(
        data.aws_availability_zones.eu_west_2.names,
        each.key
    )

    tags = {
        Name = "multiverse-${each.key}"
    }
}

resource "aws_internet_gateway" "this" {
    vpc_id = aws_vpc.this.id
    tags = {
        Name = "multiverse"
    }
}


resource "aws_route_table" "public" {
    vpc_id = aws_vpc.this.id
    tags = {
        Name = "multiverse-public"
    }
}

resource "aws_route" "public" {
    route_table_id = aws_route_table.public.id
    destination_cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.this.id
}

resource "aws_route_table_association" "public" {
    for_each = aws_subnet.public
    subnet_id = each.value.id
    route_table_id = aws_route_table.public.id
}

resource "aws_vpc_endpoint" "s3" {
    vpc_id = aws_vpc.this.id
    service_name = "com.amazonaws.eu-west-2.s3"
    tags = {
     Name = "multiverse"
    }
}

resource "aws_vpc_endpoint_route_table_association" "this" {
    route_table_id = aws_route_table.public.id
    vpc_endpoint_id = aws_vpc_endpoint.s3.id
}

resource "aws_s3_bucket" "this" {
    bucket_prefix = "mvws9-eduardo"
    force_destroy = true
    tags = {
        Name = "multiverse"
    }
}

resource "aws_s3_bucket_acl" "this" {
    bucket = aws_s3_bucket.this.id
    acl = "private"
}

resource "aws_s3_object" "this" {
    bucket = aws_s3_bucket.this.id
    key = "results.csv"
    source = "${path.module}/results.csv"
    etag = filemd5("${path.module}/results.csv")
}