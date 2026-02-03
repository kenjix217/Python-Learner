/**
 * Block-to-Text Bridge
 * Integrates Google Blockly to generate Python code
 */

export class BlocklyManager {
    constructor(containerId, editor) {
        this.containerId = containerId;
        this.editor = editor; // Monaco instance
        this.workspace = null;
    }

    async load() {
        // Load Blockly from CDN if not present
        if (!window.Blockly) {
            await this.injectScripts();
        }
        this.initWorkspace();
    }

    injectScripts() {
        return new Promise((resolve) => {
            const script = document.createElement('script');
            script.src = "https://unpkg.com/blockly/blockly.min.js";
            script.onload = () => {
                const pythonScript = document.createElement('script');
                pythonScript.src = "https://unpkg.com/blockly/python_compressed.js";
                pythonScript.onload = resolve;
                document.head.appendChild(pythonScript);
            };
            document.head.appendChild(script);
        });
    }

    initWorkspace() {
        const container = document.getElementById(this.containerId);
        container.innerHTML = ''; // Clear
        
        this.workspace = Blockly.inject(container, {
            toolbox: this.getToolbox(),
            scrollbars: true,
            trashcan: true
        });

        // Real-time code generation
        this.workspace.addChangeListener(() => {
            const code = Blockly.Python.workspaceToCode(this.workspace);
            this.editor.setValue(code);
        });
    }

    getToolbox() {
        return `
        <xml>
            <category name="Logic" colour="210">
                <block type="controls_if"></block>
                <block type="logic_compare"></block>
            </category>
            <category name="Loops" colour="120">
                <block type="controls_repeat_ext"></block>
            </category>
            <category name="Math" colour="230">
                <block type="math_number"></block>
            </category>
            <category name="Text" colour="160">
                <block type="text"></block>
                <block type="text_print"></block>
            </category>
        </xml>`;
    }
}
