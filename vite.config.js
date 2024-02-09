import {defineConfig} from "vite";
const { resolve } = require('path');

export default defineConfig({
    base: "/",
    build: {
        manifest: "manifest.json",
        outDir: resolve("./resources/static/vite"),
        rollupOptions: {
            input: {
                appJs: resolve("./resources/static/js/app.js"),
                appCss: resolve("./resources/static/css/app.css"),
            }
        }
    }
})

