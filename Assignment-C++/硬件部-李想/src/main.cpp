#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
#include <cpr/cpr.h>

int main() {
    // 读取 config.json 文件
    std::ifstream config_file("config.json");
    if (!config_file.is_open()) {
        std::cerr << "无法打开 config.json 文件" << std::endl;
        return 1;
    }

    nlohmann::json config;
    config_file >> config;
    std::string url = config["url"];

    // 使用 cpr 库访问网址
    cpr::Response response = cpr::Get(cpr::Url{url});
    if (response.status_code != 200) {
        std::cerr << "无法访问网址: " << url << std::endl;
        return 1;
    }

    // 将网页内容保存到文件
    std::ofstream output_file("webpage.html");
    if (!output_file.is_open()) {
        std::cerr << "无法创建网页文件" << std::endl;
        return 1;
    }
    output_file << response.text;

    std::cout << "网页已保存到 webpage.html" << std::endl;
    return 0;
}