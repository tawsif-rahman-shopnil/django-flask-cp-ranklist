const line1 = document.querySelector("#line1 .animated-text");
        const line2 = document.querySelector("#line2 .animated-text");
        const text1 = line1.textContent;
        const text2 = line2.textContent;
        const delay1 = 0.05; // Adjust delay as needed
        const delay2 = 0.15; // Adjust delay as needed
      
        function animateText(line, text, delay) {
          line.innerHTML = '';
          for (let i = 0; i < text.length; i++) {
            const span = document.createElement('span');
            span.textContent = text[i];
            span.style.animationDelay = `${delay * i}s`;
            span.classList.add('char');
            line.appendChild(span);
          }
        }
      
        function blinkLastLetter(line, delay) {
            const chars = line.querySelectorAll('.char');
            const lastChar = chars[chars.length - 1];
            lastChar.classList.add('blink');
            if (lastChar.textContent.trim() === _) {
                const secondLastChar = chars[chars.length - 2];
                secondLastChar.classList.add('blink');
            }
            setInterval(() => {
                lastChar.classList.toggle('blink');
                if (lastChar.textContent.trim() === _) {
                    const secondLastChar = chars[chars.length - 2];
                    secondLastChar.classList.toggle('blink');
                }
            },delay * 1000);
        }


      
        function loopAnimation() {
          animateText(line1, text1, delay1);
          animateText(line2, text2, delay2);
          blinkLastLetter(line1, delay1 * text1.length);
          blinkLastLetter(line2, delay2 * text2.length);
          // Remove the animations after they finish to prepare for the next loop
          setTimeout(() => {
            line1.innerHTML = text1;
            line2.innerHTML = text2;
          }, (Math.max(text1.length, text2.length) * delay2 + 0.5) * 1000);
        }
      
        // Run the animation loop
        setTimeout(() => {
          loopAnimation();
          setInterval(loopAnimation, (Math.max(text1.length, text2.length) * delay2 + 10) * 1000);  // Adjust interval as needed
        }, 10000);