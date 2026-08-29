export default [
  {
    files: ["**/*.js", "**/*.ts", "**/*.inline.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "script",
      parserOptions: { ecmaFeatures: { globalReturn: false } }
    },
    rules: {
      "no-duplicate-case": "error",
      "no-unreachable": "error",
      "no-unexpected-multiline": "error",
      "no-constant-condition": "warn",
      "no-dupe-keys": "error",
      "no-redeclare": "error"
    }
  }
];
