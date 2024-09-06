let currentInput = ''; // 当前输入的数字或运算符
let expression = '';   // 整个表达式

function appendNumber(number) {
    currentInput += number;
    updateDisplay(expression + currentInput);
}

function appendDecimal() {
    if (!currentInput.includes('.')) {
        currentInput += '.';
        updateDisplay(expression + currentInput);
    }
}

function appendParenthesis(parenthesis) {
    if (parenthesis === '(') {
        expression += parenthesis;
    } else if (parenthesis === ')' && expression.includes('(')) {
        expression += currentInput + parenthesis;
        currentInput = '';
    }
    updateDisplay(expression + currentInput);
}

function chooseOperation(op) {
    if (currentInput === '' && expression === '') return; // 防止首个输入为操作符
    if (currentInput === '' && expression !== '') {       // 更改最后一个操作符
        expression = expression.slice(0, -1) + op;
    } else {
        expression += currentInput + op;
    }
    currentInput = ''; // 清空当前输入，准备输入下一个数字
    updateDisplay(expression);
}

function calculate() {
    if (currentInput !== '') {
        expression += currentInput;
    }
    try {
        const result = eval(expression); // 计算表达式
        updateDisplay(result);
        expression = ''; // 清空表达式
        currentInput = result.toString(); // 将结果作为新的起点
    } catch (e) {
        updateDisplay('Error');
    }
}

function clearDisplay() {
    currentInput = '';
    expression = '';
    updateDisplay('');
}

function backspace() {
    if (currentInput !== '') {
        currentInput = currentInput.slice(0, -1);
        updateDisplay(expression + currentInput);
    } else if (expression !== '') {
        expression = expression.slice(0, -1);
        updateDisplay(expression);
    }
}

function updateDisplay(content) {
    document.getElementById('display').value = content;
}
