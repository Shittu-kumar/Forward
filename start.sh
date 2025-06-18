echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone  https://github.com/jisshubot1/Jisshu-Forward-Bot Jisshubot1/Jisshu-forward-bot 
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/jisshubot1/Jisshu-Forward-Bot -b $BRANCH /Jisshu-forward-bot
fi
cd jisshubot1/Jisshu-Forward-Bot 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
gunicorn app:app & python3 main.py
