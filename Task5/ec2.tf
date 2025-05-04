
# Look up the existing security group
data "aws_security_group" "my_security_sg" {
  name = "launch-wizard-1"
}

# EC2 creation


resource "aws_instance" "task5-demo-instance" {
  instance_name = "task5-demo-instance"
  ami           = "ami-075686beab831bb7f"
  instance_type = "t2.micro"
  availability_zone = "us-west-2b"
  key_name = "aws-keypair"
  vpc_security_group_ids = [data.aws_security_group.my_security_sg.id]

  tags = {
    Project = "internship-task5"
    Environment = "Dev"

  }
}
