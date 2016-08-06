import psycopg2

def db():
	conn = psycopg2.connect("dbname=newspade user=cmwaura host=localhost password=7PFTcrisG@PD")
	cur = conn.cursor()
	print "iam in"
	cur.execute("SELECT * from mysites_bbcnews;")
	print "lets go"
	cur.fetchone()
db()