
---

## 📄 `README-amazon.md`

```markdown
# 🚀 Risk & Scope Copilot (Amazon Edition)

**Amazon-ready multi-agent framework**, aligned with *Working Backwards* methodology (One-pager, 6-pager, PRFAQ, OP1/OP2).  
Built for **TPMs, PMTs, and engineers** to accelerate product decisions.

---

## 💎 Value for Amazon
- Drafts **PRFAQ / One-pager / 6-pager** automatically.  
- Generates **RACI, ADRs, Risks, Scope Options** with diffs and evidence.  
- Accelerates **OP1 / OP2 reviews** with data-backed insights.  
- Provides **status dashboard** across teams and dependencies.

---

## ⚙️ Amazon Tech Stack
- **AI Agents:** Bedrock (Claude / Titan)  
- **Compute:** ECS / Lambda  
- **Storage:** S3, DynamoDB  
- **ML:** SageMaker + Bedrock  
- **CI/CD:** CodePipeline  
- **Monitoring:** CloudWatch + CloudTrail  
- **Security:** VPC Endpoints, KMS, IAM, Secrets Manager  

---

## 🏗️ Architecture

```mermaid
flowchart TB
  UI[Web UI] --> API[FastAPI on ECS/Lambda]
  API --> AGENTS[Bedrock Agents via MCP]
  API --> S3
  API --> DDB[(DynamoDB)]
  API --> CW[CloudWatch]
  API --> CT[CloudTrail]
  UI <-.diffs/status.-> S3
