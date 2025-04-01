import json
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
import os
import sys 
sys.path.append("./Cohere")
from template import TEMPLATE



# Khởi tạo mô hình Gemini
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-pro"
# )
llm = ChatCohere()

def cohere_response(cv_text, file_path, full_file_path) -> dict:
    template = PromptTemplate(template=TEMPLATE, input_variables=["cv_text", "file_path", "full_file_path"])
    chain = template | llm 
    output = chain.invoke({
        "file_path": file_path,
        "cv_text": cv_text,
        "full_file_path": full_file_path
    })
    print(file_path)
    output = json.loads(output.content)
    return output


if __name__ == "__main__":

    current_path = os.getcwd()
    file_path = "Le-Hong-Lam-TopCV.vn-160822.103239.pdf"
    full_file_path = current_path 

    cv_text ="""
            LE KHANH LY DATA ANALYST 6 Female oe  
            098 483 9919 09101998  
            khanhlyktqt98@gmail.com 9 
            21 Le Van Luong Thanh Xuan District Ha Noi City 66 - 
            Short-term goals Cultivate and improve practical knowledge along with a passion for data research successfully complete the requirements assigned by the team leader Build Dashboard to report business results plan and predict business results for the Companys products. 
            - Long-term goals Continue to learn improve thinking ability in business analysis programming languages such as Python R... set a goal in the next 5-7 years to become an expert data scientist 
            National Economics University Major International Economy Soft Skills 102016 - 082020 - 
            Self-study research information gathering Data Analytics Basic Data Analytics analysis and presentation skills. 
            042022 - 062022 - Team work and team leader skills - 
            Basic process of data analysis Collecting cleaning data mining basic model ste building visualization. 
            Concepts of Data warehouses Database Relational Computer Skills  Database Management System RDBMS NoSQL ETL...  
            Have basic computer literacy skills such Power BI Basic Course on Coursera Data Analytics as Word Excel Power Point Outlook Power Bl 042022 - 062022   English - Split rename columns add columns delete columns and change data types merge Comunicating reading and speaking basic English data join data. Introduce charts create dashboards reports with images SQL Functions in W3SCHOOL SQL  ACTIVITIES 042022 - 062022 - Concepts of 40 basic functions in SQL - Won the third prize in scientific research at the university. Theme Economic cooperationbetween  WORK EXPERIENCE Vietnam and Chile throughthe Comprehensive and ProgressiveAgreement for Trans-PacificPartnership Bambooviet Logistics.Co Ltd Sale Executive and Customs Declaration Staff CPTPP 072019 - 042022 . - Volunteer for the Studentspropagate Prevention - Introduce the companys air freight and sea freight services answer of societysvices and HIVAIDS customers questions about customs procedures import and export procedures. Coordinating with the documentation department to make the customs declaration check the accuracy of the shipment and clear customs procedures track domestic and international shipping. Guang Chau Womens Fashion Shop Shop Manager 102021 - NOW - Finding sources developing Facebook page. Answering customers questions receiving purchase orders packaging goods revenue and expense statistics. Chuyn nganh Kinh t Quoc t  102016 - 082020 Dai hoc Kinh t Quc dan Data Analytics  042022 - 062022 Kha hoc co ban v phan tich dir liu trn Coursera Data Analytics Basic - Quy trinh co ban phan tich d liu Thu thap lam sach khai thac d liu xay dung model co ban visualization - Cac khai nim v Data warehouses Database H thong quan tri co so d ligu RDBMS ETL... Data Analytics  042022 - 062022 Kha hoc Chuan bi Lam sach Bin doi dir ligu bang Power Bl trn Coursera - Tach d6i tn cdc ct thm ct xa ct va thay di kiu d liu hop nhat d liu ni d liu Data Analytics  042022 - 062022 Kha hoc xay dung trang tong quan trongPower BI trn Coursera - Gidi thiu cdc biu dd tao dashboard bao cdo bang hinh anh SQL  042022 - 062022 Cac ham trong ng6n ngif truy van SQL trnw3school - Khai nim cdc ham co ban trong SQL e KINH NGHIEM LAM VIEC Nhan vin Kinh doanh va Khai bao Hai Quan  072019 - 042022 Cong ty TNHH Kho van Bambooviet - Gidi thiu dich vu van chuyn hang hda quc t cia Cong ty gidi dap cdc van d thac mac cla khach hang v thu tuc Hai quan quy trinh xuat nhap khau hang ha - Phi hop vi phong ching tl d ln to khai Hai quan kim tra tinh chinh xc 16 hang va lam thu tuc thong quan theo di van chuyn ni dia va quc t. Quan ly Shop  102021 - HIEN NAY Shop quan do thoi trang nit Quang Chau - Tu tim ngudn hang x4y dung va phat trin page ndi dung hinh anh - Tu van cho khach cht don dng hang thong k doanh thu chi phi. L@ Khanh ly Chuyn vin phan tich dit liu THONG TIN 09101998 098 483 9919 khanhlyktqt98@gmail.com O@O@O 21 L Van Luong Quan Thanh Xuan Ha Noi e Muc tiu ngh nghip - Muc tiu ngan han Trau di hoan thin kin thc thuc chin cling vdi dam m nghin cttu voi d liu hoan thanh that tt yu cau do team leader giao Xay dung Dashboard bdo cdo kt qua kinh doanh lap k hoach va du doan kt qua kinh doanh cho nhiing san pham cua Cng ty. - Muc tiu dai han Tip tuc hoc hdi trau di kha nang tu duy trong phan tich kinh doanh ng6n ngf lap trinh nhu Python R... dt muc tiu tl 5-7 nim tdi tro thanh chuyn gia khoa hoc df liu. C KY NANG Ky nang mem - K nang tu hoc nghin ctfu thu thap thong tin phan tich va trinh bay. - Kj nang lam vic nhom quan ly nhm Tin hoc van phong - SU dung thanh thao cdc cong cu Word Excel Power Point Outlook Power BI Ting Anh Giao tip doc vit Ting Anh co ban  topev.vn
    """
    output = cohere_response(cv_text=cv_text, file_path=file_path, job_name="AI engineer", full_file_path=current_path)
    print(output)


<video id="input_video" autoplay muted playsinline></video>
<canvas id="output_canvas"></canvas>
<img id="clothes" src="/images/shirt.png" style="display:none">

<script src="https://cdn.jsdelivr.net/npm/@mediapipe/selfie_segmentation/selfie_segmentation.js"></script>
<script>
const video = document.getElementById('input_video');
const canvas = document.getElementById('output_canvas');
const ctx = canvas.getContext('2d');
const clothes = document.getElementById('clothes');

const selfieSegmentation = new SelfieSegmentation({locateFile: (file) => 
  `https://cdn.jsdelivr.net/npm/@mediapipe/selfie_segmentation/${file}`});
selfieSegmentation.setOptions({ modelSelection: 1 });

selfieSegmentation.onResults(results => {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  ctx.drawImage(results.image, 0, 0, canvas.width, canvas.height);
  // Overlay áo vào body (vị trí bạn điều chỉnh theo ý)
  ctx.drawImage(clothes, canvas.width/2 - 100, canvas.height/2 - 150, 200, 200);
});

navigator.mediaDevices.getUserMedia({video: true}).then(stream => {
  video.srcObject = stream;
  video.play();
  function process() {
    selfieSegmentation.send({image: video});
    requestAnimationFrame(process);
  }
  process();
});
</script>
