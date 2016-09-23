import urllib
import urllib.request


def main():
    url = "http://real-chart.finance.yahoo.com/table.csv?s=TIF&a=09&b=9&c=2014&d=09&e=9&f=2015&g=d&ignore=.csv"

    htmlfile = ""
    htmlfile = urllib.request.urlopen(url, timeout=20)
    htmltext = str(htmlfile.read())

    htmltext = htmltext.replace("'", "")
    htmlrecords = htmltext.split("\\n")


    sfile = open("text.csv", "w")
    for x in htmlrecords:
        print(x, file=sfile)
    sfile.close()

main()
