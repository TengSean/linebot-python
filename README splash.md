# Splash set up

Run the Splash docker
<pre><code>$ docker run -p 8050:8050 scrapinghub/splash</code></pre>

Run scrapy spyder
<pre><code>$ scrapy crawl {SPYDER_NAME}</code></pre>

(Optional)Run the Splash-jupyter docker
<pre><code>$ docker run -e DISPLAY=unix$DISPLAY \
             -v /tmp/.X11-unix:/tmp/.X11-unix \
             -v $XAUTHORITY:$XAUTHORITY \
             -e XAUTHORITY=$XAUTHORITY \
             -p 8888:8888 \
             -it scrapinghub/splash-jupyter --disable-xvfb</code></pre>

# Terimanl setting
<pre><code>"workbench.colorCustomizations": {
        "terminal.background":"#2B2B2B",
        "terminal.foreground":"#E6E1DC",
        "terminalCursor.background":"#E6E1DC",
        "terminalCursor.foreground":"#E6E1DC",
        "terminal.ansiBlack":"#2B2B2B",
        "terminal.ansiBlue":"#6D9CBE",
        "terminal.ansiBrightBlack":"#5A647E",
        "terminal.ansiBrightBlue":"#6D9CBE",
        "terminal.ansiBrightCyan":"#519F50",
        "terminal.ansiBrightGreen":"#A5C261",
        "terminal.ansiBrightMagenta":"#B6B3EB",
        "terminal.ansiBrightRed":"#DA4939",
        "terminal.ansiBrightWhite":"#F9F7F3",
        "terminal.ansiBrightYellow":"#FFC66D",
        "terminal.ansiCyan":"#519F50",
        "terminal.ansiGreen":"#A5C261",
        "terminal.ansiMagenta":"#B6B3EB",
        "terminal.ansiRed":"#DA4939",
        "terminal.ansiWhite":"#E6E1DC",
        "terminal.ansiYellow":"#FFC66D"
      },
</code></pre>