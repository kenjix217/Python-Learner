/**
 * Arcade Mode
 * Logic for Bug Hunter and Visual Art Playground
 */

export class Arcade {
    constructor(codeEditor) {
        this.codeEditor = codeEditor;
        this.currentMode = null;
    }

    /**
     * Start Bug Hunter Level
     */
    loadBugHunterLevel(levelIndex) {
        const levels = [
            {
                title: "The Broken Print",
                buggyCode: `print("Hello World"`,
                hint: "Something is missing at the end!",
                solution: `print("Hello World")`
            },
            {
                title: "Indentation Nation",
                buggyCode: `def greet():\nprint("Hi there!")`,
                hint: "Python needs indentation inside functions.",
                solution: `def greet():\n    print("Hi there!")`
            },
            {
                title: "Variable Vanish",
                buggyCode: `name = "Alice"\nprint(nme)`,
                hint: "Check the spelling of the variable name.",
                solution: `name = "Alice"\nprint(name)`
            }
        ];

        const level = levels[levelIndex] || levels[0];
        this.codeEditor.setCode(level.buggyCode);
        return level;
    }

    /**
     * Start Visual Art Playground
     */
    loadVisualArt() {
        const artTemplate = `import matplotlib.pyplot as plt
import numpy as np

# Create a spiral
t = np.linspace(0, 10*np.pi, 500)
x = t * np.cos(t)
y = t * np.sin(t)

plt.figure(figsize=(6,6))
plt.plot(x, y, color='purple', linewidth=2)
plt.title("Generative Art")
plt.axis('off')
plt.show()`;
        
        this.codeEditor.setCode(artTemplate);
    }
}
