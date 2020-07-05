# Splash set up

Run the Splash docker
<pre><code>docker run -p 8050:8050 scrapinghub/splash</code></pre>

Run the Splash-jupyter docker
<pre><code>$ docker run -e DISPLAY=unix$DISPLAY \
             -v /tmp/.X11-unix:/tmp/.X11-unix \
             -v $XAUTHORITY:$XAUTHORITY \
             -e XAUTHORITY=$XAUTHORITY \
             -p 8888:8888 \
             -it scrapinghub/splash-jupyter --disable-xvfb</code></pre>