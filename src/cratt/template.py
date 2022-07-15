ADDED_DIRECTORY = [
    'assets',
    'components',
    'context',
    'data',
    'hooks',
    'pages',
    'services',
    'types',
    'utils',
]

CHANGED_FILE = ['App.tsx', 'index.tsx', 'index.css', 'react-app-env.d.ts']

APP = """
import { useState, useEffect } from 'react';

export function App() {
  return (
    <div className='App'>
      <h1>Hello World</h1>
    </div>
  );
}
"""

INDEX = """
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { App } from './App';
import './index.scss';

const container = document.getElementById('root') as HTMLElement;
const root = createRoot(container);

root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
"""

SASS = """
@tailwind base;
@tailwind components;
@tailwind utilities;
"""

ES_LINT_CONFIG = """
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": [
    "airbnb",
    "airbnb-typescript",
    "plugin:react/recommended",
    "plugin:react/jsx-runtime",
    "plugin:@typescript-eslint/recommended",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "project": "./tsconfig.json",
    "ecmaFeatures": {
      "jsx": true
    },
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "rules": {
    "@typescript-eslint/quotes": ["error", "single", { "avoidEscape": true }],
    "@typescript-eslint/semi": ["warn", "always"],
    "@typescript-eslint/consistent-type-imports": "error",
    "@typescript-eslint/comma-dangle": ["error", "never"],
    "@typescript-eslint/no-unused-vars": "warn",
    "@typescript-eslint/no-use-before-define": "off",
    "@typescript-eslint/no-non-null-assertion": "off",
    "@typescript-eslint/no-unused-expressions": "off",
    "@typescript-eslint/prefer-nullish-coalescing": "error",
    "@typescript-eslint/explicit-function-return-type": "error",
    "react/prop-types": "off",
    "react/button-has-type": "off",
    "react/no-array-index-key": "off",
    "react/jsx-props-no-spreading": "off",
    "react/jsx-no-constructed-context-values": "off",
    "jsx-quotes": ["error", "prefer-single"],
    "curly": ["error", "multi"],
    "no-console": "warn",
    "linebreak-style": "off",
    "no-nested-ternary": "off",
    "react/self-closing-comp": "warn",
    "react/require-default-props": "off",
    "react/no-unescaped-entities": "off",
    "import/no-default-export": "error",
    "import/prefer-default-export": "off",
    "import/order": [
      "error",
      {
        "groups": ["builtin", "external", "parent", "sibling", "index", "type"]
      }
    ]
  }
}
"""

ES_LINT_IGNORE = """
tailwind.config.js
postcss.config.js
"""

PRETTIER_CONFIG = """
{
  "singleQuote": true,
  "jsxSingleQuote": true,
  "trailingComma": "none"
}
"""

PRETTIER_IGNORE = """
# Ignore artifacts:
build
coverage
"""
