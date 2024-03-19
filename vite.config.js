import {defineConfig} from "vite";
import react from "@vitejs/plugin-react";

const {resolve} = require('path');

export default defineConfig({
    base: "/",
    plugins: [react()],
    build: {
        manifest: "manifest.json",
        outDir: resolve("./resources/static/vite"),
        rollupOptions: {
            input: {
                appJs: resolve("./resources/static/js/app.js"),
                appCss: resolve("./resources/static/css/app.css"),
                outCss: resolve("./resources/static/css/output.css")
            }
        }
    }
})

