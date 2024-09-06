#include <iostream>
#include <fstream>
#include <string>

#include <nlohmann/json.hpp>
#include <cpr/cpr.h>
#include <filesystem>

using namespace std;
using json = nlohmann::json;
namespace fs = std::filesystem;

int main() {
    fs::path currentPath = fs::current_path();
    fs::path configPath = currentPath.parent_path().parent_path().parent_path().parent_path() / "config.json";

    // 读取config.json
    ifstream configFile(configPath);
    if (!configFile.is_open()) {
        cerr << "Unable to open config.json" << endl;
        return 1;
    }

    json config;
    configFile >> config;
    configFile.close();

    string url = config["url"];

    // 使用cpr访问网址
    cpr::Response r = cpr::Get(cpr::Url{url});
    if (r.status_code == 200) {
        // 将网页保存到当前目录
        ofstream outputFile("output.html");
        if (outputFile.is_open()) {
            outputFile << r.text;
            outputFile.close();
            cout << "Web page saved to output.html" << endl;
        } else {
            cerr << "Unable to open output.html for writing" << endl;
            return 1;
        }
    } else {
        cerr << "Failed to retrieve web page, status code " 
            << r.status_code << endl;
        return 1;
    }

    return 0;
}
